from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db = SQLAlchemy()
DB_NAME = "holiday.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'coursework'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .authentication import authentication

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(authentication,url_prefix='/')
    
    return app

