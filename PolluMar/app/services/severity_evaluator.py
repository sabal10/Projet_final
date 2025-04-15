class SeverityEvaluator:
    def evaluate(self, pollution_type: str, quantity: float) -> str:
        if pollution_type == "Plastiques":
            if quantity > 50:
                return "Urgent"
            elif quantity >= 10:
                return "Modéré"
            else:
                return "Faible"

        elif pollution_type == "Hydrocarbures":
            if quantity > 20:
                return "Urgent"
            elif quantity >= 5:
                return "Modéré"
            else:
                return "Faible"

        elif pollution_type == "Déchets Chimiques":
            if quantity > 500:
                return "Urgent"
            elif quantity >= 100:
                return "Modéré"
            else:
                return "Faible"

        else:
            return "Inconnue"
