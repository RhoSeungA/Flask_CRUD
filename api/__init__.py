from flask import Flask
from flask_restful import Api
from api.database import db
from api.routes import init_routes
from api.models.user import User

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        SQLALCHEMY_COMMIT_ON_TEARDOWN = True,
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:',
    )
    api = Api(app)
    
    db.init_app(app)

    with app.app_context():
        db.create_all()
        set_default_user()

    init_routes(api)

    return app


def set_default_user():
    try:
        users = [
            User(id=1, email='a@gmail.com', phone_number='010-1234-5678'),
            User(id=2, email='b@gmail.com', phone_number='010-1235-5678')
        ]
        db.session.add_all(users)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()