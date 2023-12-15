from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#pip install SQLAlchemy
#pip install flask-sqlalchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///datos.db'
    app.config['SECRET_KEY'] = '1qa2ws3ed4rf5tg6yh7uj8ik9ol0pñ'

    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

    from .routes import main
    app.register_blueprint(main)

    login_manager.init_app(app) 

    @login_manager.user_loader
    def load_user(user_id):
        return models.Persona.query.get(int(user_id))
    
    login_manager.login_view = 'main.login'

    return app



