from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize application
app = Flask(__name__)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

# Initialize Flask Sql Alchemy
db = SQLAlchemy(app)

# Initialize Flask Migrate
migrate = Migrate(app, db)

# Inirialize Flask Bcrypt
bcrypt = Bcrypt(app)

# Register blue prints
from app.authenticate.views import auth

app.register_blueprint(auth)
