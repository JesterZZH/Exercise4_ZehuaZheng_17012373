from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

# The SQLAlchemy object is defined globally
db = SQLAlchemy()


def create_app(config_class=DevConfig):
    """
    Creates an application instance to run
    :return: A Flask object
    """
    app = Flask(__name__)

    # Configure app wth the settings from config.py
    app.config.from_object(config_class)

    # Initialise the database so that the app can use it
    db.init_app(app)

    with app.app_context():
        db.Model.metadata.reflect(db.engine)

    # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app
