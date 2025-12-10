from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

from typing_extensions import Any

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ILikeToEatMacarons123!'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    return app


def create_database(app: Any):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database')
