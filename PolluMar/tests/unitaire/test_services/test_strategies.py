# Fichier : tests/unitaire/test_services/test_strategies.py

import pytest
from app.services.severity_strategy import (
    PlasticSeverityStrategy,
    HydrocarbonSeverityStrategy,
    ChemicalSeverityStrategy
)

# ✅ Test pour la stratégie Plastiques
def test_plastic_strategy():
    strategy = PlasticSeverityStrategy()
    assert strategy.evaluate(5) == "Faible"
    assert strategy.evaluate(15) == "Modéré"
    assert strategy.evaluate(80) == "Urgent"

# ✅ Test pour la stratégie Hydrocarbures
def test_hydrocarbon_strategy():
    strategy = HydrocarbonSeverityStrategy()
    assert strategy.evaluate(3) == "Faible"
    assert strategy.evaluate(10) == "Modéré"
    assert strategy.evaluate(25) == "Urgent"

# ✅ Test pour la stratégie Déchets Chimiques
def test_chemical_strategy():
    strategy = ChemicalSeverityStrategy()
    assert strategy.evaluate(50) == "Faible"
    assert strategy.evaluate(200) == "Modéré"
    assert strategy.evaluate(600) == "Urgent"
