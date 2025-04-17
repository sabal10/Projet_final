# 📦 Variables
PYTHON = python
PYTEST = pytest
FLASK_APP = app
APP_DIR = app
TESTS_DIR = tests
COV_REPORT = --cov=$(APP_DIR) --cov-report=term

# 📌 Lancer l'application
run:
	@echo "🚀 Lancement de l'application Flask..."
	$(PYTHON) -m $(FLASK_APP)

# 🧪 Tests unitaires
test-unit:
	@echo "🧪 Tests unitaires..."
	$(PYTEST) $(TESTS_DIR)/unitaire

# 🔌 Tests d’intégration
test-integration:
	@echo "🔌 Tests d'intégration..."
	$(PYTEST) $(TESTS_DIR)/integration

# 🤖 Tests E2E
test-e2e:
	@echo "🤖 Tests end-to-end..."
	$(PYTEST) $(TESTS_DIR)/e2e

# 🧪 Tous les tests avec couverture
test-all:
	@echo "📊 Tous les tests avec couverture..."
	$(PYTEST) $(COV_REPORT)

# 🧼 Nettoyage des fichiers temporaires
clean:
	@echo "🧹 Suppression des fichiers .pyc et __pycache__..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

# 🧼 Réinitialisation de la base SQLite
reset-db:
	@echo "🗑️ Suppression de pollution.db..."
	rm -f pollution.db

# ✅ Tout en un : clean + tests
full-check:
	make clean
	make test-all
