import sys
import os

# Ajoute le chemin vers le dossier "app" pour permettre l'import des modules internes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../app')))

import pytest
from services.severity_evaluator import SeverityEvaluator

# Fixture pour créer une instance unique de l'évaluateur de gravité
@pytest.fixture
def evaluator():
    return SeverityEvaluator()

# Vérifie que le score faible pour les plastiques retourne "Faible"
def test_plastiques_faible(evaluator):
    severity = evaluator.evaluate("Plastiques", 5)
    assert severity == "Faible"

# Vérifie que le score modéré pour les plastiques retourne "Modéré"
def test_plastiques_moderer(evaluator):
    severity = evaluator.evaluate("Plastiques", 25)
    assert severity == "Modéré"

# Vérifie que le score élevé pour les plastiques retourne "Urgent"
def test_plastiques_urgent(evaluator):
    severity = evaluator.evaluate("Plastiques", 80)
    assert severity == "Urgent"

# Vérifie le comportement pour un type inconnu
def test_type_inconnu(evaluator):
    severity = evaluator.evaluate("Autre", 50)
    assert severity == "Inconnue"
