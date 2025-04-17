@echo off
setlocal

REM =============================
REM 🎯 Script Make pour PolluMar
REM =============================

REM Lancement de l'application
if "%1"=="run" (
    echo 🚀 Lancement de l'application Flask...
    python -m app
    exit /b
)

REM Tests unitaires
if "%1"=="test-unit" (
    echo 🔬 Lancement des tests unitaires...
    pytest tests/unitaire
    exit /b
)

REM Tests d'intégration
if "%1"=="test-integration" (
    echo 🔁 Lancement des tests d'intégration...
    pytest tests/integration
    exit /b
)

REM Tests E2E
if "%1"=="test-e2e" (
    echo 🌐 Lancement des tests End-to-End...
    pytest tests/e2e
    exit /b
)

REM Tests complets avec couverture
if "%1"=="test-all" (
    echo 🧪 Tests complets avec couverture...
    pytest --cov=app --cov-report=term
    exit /b
)

REM Aide
echo ❌ Commande non reconnue.
echo.
echo ✅ Commandes disponibles :
echo ----------------------------
echo make.bat run               ^| Lancer l'application Flask
echo make.bat test-unit         ^| Lancer les tests unitaires
echo make.bat test-integration  ^| Lancer les tests d'intégration
echo make.bat test-e2e          ^| Lancer les tests end-to-end
echo make.bat test-all          ^| Lancer tous les tests avec couverture

endlocal
