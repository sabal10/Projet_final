from datetime import datetime
from app.models.database import Database

class NotificationService:
    """
    Service responsable de l'envoi de notifications lors d'un signalement.
    Cette version simule l'envoi par affichage console et enregistre dans la base.
    """

    def send(self, data):
        required_fields = [
            "name", "pollution_type", "description", "location",
            "quantity", "responder_name", "responder_email"
        ]

        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Champ obligatoire manquant : {field}")

        # Générer l'heure actuelle de création
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        db = Database()

        # 🔍 Vérification de doublon (exact match sur les champs clés dans les dernières minutes)
        existing = db.execute_query("""
            SELECT * FROM reports
            WHERE name = ? AND pollution_type = ? AND location = ?
              AND responder_name = ? AND responder_email = ?
              AND status = 'En attente'
              ORDER BY created_at DESC
            LIMIT 1
        """, (
            data["name"], data["pollution_type"], data["location"],
            data["responder_name"], data["responder_email"]
        ))

        if existing:
            print("⚠️ Doublon détecté : ce signalement existe déjà récemment.")
            return  # ⛔ Ne pas insérer à nouveau

        # Gravité par défaut si absente
        severity = data.get("severity", "Inconnue")

        # ✅ Insertion dans la base
        db.execute_query("""
            INSERT INTO reports (
                name, pollution_type, description, location, quantity,
                severity, status, responder_name, responder_email,
                created_at, resolved_at, comment
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL)
        """, (
            data["name"], data["pollution_type"], data["description"], data["location"],
            data["quantity"], severity, "En attente",
            data["responder_name"], data["responder_email"],
            created_at
        ))

        print("\n📢 Notification envoyée avec succès ! Détails :")
        print(f"- Déclarant : {data['name']}")
        print(f"- Type : {data['pollution_type']}")
        print(f"- Description : {data['description']}")
        print(f"- Lieu : {data['location']}")
        print(f"- Quantité : {data['quantity']}")
        print(f"- Gravité : {severity}")
        print(f"- À : {data['responder_name']} ({data['responder_email']})\n")
