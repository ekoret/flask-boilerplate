from flask import Flask

from flask_server.extensions import db, migrate, jwt


def create_app():
    app = Flask(__name__)

    # Configs
    app.config.from_prefixed_env()

    # Models
    from flask_server.models import User
    from flask_server.models import Credential

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Blueprints/Routes
    from flask_server.routes import user
    from flask_server.routes import auth

    app.register_blueprint(user.user)
    app.register_blueprint(auth.auth)

    return app
