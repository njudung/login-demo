from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

__version__ = "0.1.0"

app = Flask(__name__, instance_relative_config=False)
app.config.from_object("config.Config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)

import login_demo.routes, login_demo.models  # noqa: E402, F401
