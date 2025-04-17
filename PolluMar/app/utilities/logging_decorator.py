import functools
import datetime

def logging_decorator(func):
    """
    Decorateur pour journaliser l'execution d'une fonction :
    - Affiche les arguments passes
    - Affiche le resultat retourne, meme si c'est None
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGING] 📌 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Appel de {func.__name__} avec args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOGGING] ✅ Resultat de {func.__name__} : {result if result is not None else 'Aucun (None)'}")
        return result
    return wrapper
