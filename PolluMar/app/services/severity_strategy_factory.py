from app.services.severity_strategy import (
    PlasticSeverityStrategy,
    HydrocarbonSeverityStrategy,
    ChemicalSeverityStrategy,
    SeverityStrategy
)

class SeverityStrategyFactory:
    @staticmethod
    def get_strategy(pollution_type: str) -> SeverityStrategy:
        strategies = {
            "plastiques": PlasticSeverityStrategy,
            "hydrocarbures": HydrocarbonSeverityStrategy,
            "déchets chimiques": ChemicalSeverityStrategy
        }

        key = pollution_type.strip().lower()
        strategy_class = strategies.get(key)

        return strategy_class() if strategy_class else None
