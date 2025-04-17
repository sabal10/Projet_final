from app.utilities.logging_decorator import logging_decorator

@logging_decorator
def dummy_function(x, y):
    return x + y

@logging_decorator
def dummy_void_function():
    print("Fonction sans retour")

def test_log_execution_retour(capsys):
    """
    Verifie que le decorateur affiche le nom de la fonction et son retour.
    """
    result = dummy_function(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "[LOGGING]" in captured.out
    assert "Appel de dummy_function" in captured.out
    assert (
        "Resultat de dummy_function : 5" in captured.out
        or "Resultat de dummy_function : Aucun (None)" in captured.out
    )

def test_log_execution_sans_retour(capsys):
    """
    Verifie que le decorateur fonctionne sur une fonction sans valeur de retour.
    """
    dummy_void_function()
    captured = capsys.readouterr()

    assert "[LOGGING]" in captured.out
    assert "Appel de dummy_void_function" in captured.out
    assert (
        "Resultat de dummy_void_function : None" in captured.out
        or "Resultat de dummy_void_function : Aucun (None)" in captured.out
    )

