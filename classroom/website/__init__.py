# make website python package
from flask import Flask


def create_app():
    app = Flask(__name__)  # name of file
    app.config['SECRET_KEY'] = 'Hello my friend 956'  # secure data and cookie

    from .views import views
    from .auth import auth

    # register
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
