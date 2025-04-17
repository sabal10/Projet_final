# 📁 tests/e2e/test_logging_decorator_e2e.py

from app.utilities.logging_decorator import logging_decorator

@logging_decorator
def fonction_testee(x, y):
    return x * y

@logging_decorator
def fonction_sans_retour():
    print("Traitement sans retour")

def test_logging_decorator_avec_retour(capsys):
    result = fonction_testee(4, 5)
    captured = capsys.readouterr()

    assert result == 20
    assert "[LOGGING]" in captured.out
    assert "Appel de fonction_testee" in captured.out
    assert (
        "Resultat de fonction_testee : 20" in captured.out
        or "Resultat de fonction_testee : Aucun (None)" in captured.out
    )

def test_logging_decorator_sans_retour(capsys):
    fonction_sans_retour()
    captured = capsys.readouterr()

    assert "[LOGGING]" in captured.out
    assert "Appel de fonction_sans_retour" in captured.out
    assert (
        "Resultat de fonction_sans_retour : None" in captured.out
        or "Resultat de fonction_sans_retour : Aucun (None)" in captured.out
    )
