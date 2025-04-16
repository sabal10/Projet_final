# 📁 tests/unitaire/test_services/test_state_pattern.py

import pytest
from app.services.states.signalement import Signalement
from app.services.states.en_attente_state import EnAttenteState
from app.services.states.resolu_state import ResoluState

def test_etat_initial_en_attente():
    data = {
        "pollution_type": "Hydrocarbures",
        "location": "Québec",
        "description": "Fuite lente détectée"
    }
    signalement = Signalement(data)
    assert isinstance(signalement.state, EnAttenteState)
    assert signalement.data["status"] == "En attente"

def test_traitement_en_attente(capsys):
    data = {
        "pollution_type": "Hydrocarbures",
        "location": "Québec",
        "description": "Fuite lente détectée"
    }
    signalement = Signalement(data)
    statut = signalement.traiter()
    captured = capsys.readouterr()

    assert "[EnAttenteState]" in captured.out
    assert "Traitement en attente" in captured.out
    assert statut == "En attente"
    assert signalement.data["status"] == "En attente"

def test_changement_etat_vers_resolu(capsys):
    data = {
        "pollution_type": "Plastique",
        "location": "Montréal",
        "description": "Pollution plastique visible"
    }
    signalement = Signalement(data)
    signalement.set_state(ResoluState())

    statut = signalement.traiter()
    captured = capsys.readouterr()

    assert "[ResoluState]" in captured.out
    assert "traité et archivé" in captured.out or "résolu" in captured.out
    assert statut == "Résolu"
    assert signalement.data["status"] == "Résolu"
