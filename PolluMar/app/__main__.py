
# app/__main__.py
#from app.models.database import conn
from app import create_app  # On importe l'application via la factory

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
