# Fichier : app/services/severity_strategy_factory.py

from app.services.severity_strategy import (
    PlasticSeverityStrategy,
    HydrocarbonSeverityStrategy,
    ChemicalSeverityStrategy,
    SeverityStrategy
)

# 🎯 Cette classe applique le principe de la Factory
# Elle sélectionne dynamiquement la bonne stratégie selon le type de pollution
class SeverityStrategyFactory:
    @staticmethod
    def get_strategy(pollution_type: str) -> SeverityStrategy:
        if pollution_type == "Plastiques":
            return PlasticSeverityStrategy()
        elif pollution_type == "Hydrocarbures":
            return HydrocarbonSeverityStrategy()
        elif pollution_type == "Déchets Chimiques":
            return ChemicalSeverityStrategy()
        else:
            return None  # Aucune stratégie disponible pour ce type
