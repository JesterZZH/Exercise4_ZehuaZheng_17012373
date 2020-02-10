from flask import Flask
from config import DevConfig



def create_app(config_class=DevConfig):
   """
    Creates an application instance to run
    :return: A Flask object
    """
   app = Flask(__name__)

   # Configure app wth the settings from config.py
   app.config.from_object(config_class)

   # Register Blueprints
   from app.main.routes import bp_main
   app.register_blueprint(bp_main)


   return app