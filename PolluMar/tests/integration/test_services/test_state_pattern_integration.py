# 📁 tests/integration/test_services/test_state_pattern_integration.py

import pytest
from app.services.states.signalement import Signalement
from app.services.states.en_attente_state import EnAttenteState
from app.services.states.resolu_state import ResoluState

def test_etat_par_defaut_est_en_attente():
    """
    Vérifie que tout nouveau signalement a comme état initial 'EnAttenteState'.
    """
    data = {
        "pollution_type": "Hydrocarbures",
        "location": "Sept-Îles",
        "description": "Fuite de carburant détectée"
    }
    signalement = Signalement(data)
    assert isinstance(signalement.state, EnAttenteState)
    assert signalement.data["status"] == "En attente"

def test_transition_etat_en_attente_vers_resolu():
    """
    Vérifie la transition d’un état 'En attente' à 'Résolu' en intégration.
    """
    data = {
        "pollution_type": "Déchets chimiques",
        "location": "Port de Montréal",
        "description": "Substance toxique déversée",
        "status": "En attente"
    }
    signalement = Signalement(data)

    # État initial
    assert signalement.data["status"] == "En attente"

    # Transition vers état 'Résolu'
    signalement.set_state(ResoluState())
    result = signalement.traiter()

    # Vérifie que le traitement a mis à jour le statut
    assert result == "Résolu"
    assert signalement.data["status"] == "Résolu"
