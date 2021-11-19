from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'badussy'

    from .views import views
    from .authentication import authentication

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(authentication,url_prefix='/')
    
    return app