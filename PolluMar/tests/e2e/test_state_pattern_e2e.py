# 📁 tests/e2e/test_state_pattern_e2e.py

import pytest
from app.services.states.signalement import Signalement
from app.services.states.resolu_state import ResoluState

def test_e2e_signalement_processus_complet(capsys):
    """
    Test end-to-end simulant la vie complète d’un signalement.
    """
    data = {
        "pollution_type": "Déchets chimiques",
        "location": "Îles de la Madeleine",
        "description": "Déversement important observé"
    }

    # Étape 1 : Création
    signalement = Signalement(data)
    assert signalement.data["status"] == "En attente"

    # Étape 2 : Traitement initial
    statut_initial = signalement.traiter()
    assert statut_initial == "En attente"

    # Étape 3 : Passage à l'état résolu
    signalement.set_state(ResoluState())
    statut_final = signalement.traiter()
    assert statut_final == "Résolu"

    # Vérification sortie console
    captured = capsys.readouterr()
    assert "Traitement en attente" in captured.out or "⏳" in captured.out
    assert "Signalement traité et archivé" in captured.out or "Signalement résolu" in captured.out
