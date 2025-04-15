import os
from flask import Flask

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))  # 📁 chemin absolu vers app/
    template_dir = os.path.join(base_dir, "templates")
    static_dir = os.path.join(base_dir, "static")

    app = Flask(
        __name__,
        template_folder=template_dir,
        static_folder=static_dir
    )
  #  app.config.from_object("config.DevelopmentConfig")


    return app