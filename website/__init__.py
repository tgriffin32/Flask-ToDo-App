from flask import Flask

def create_app():
    app = Flask(__name__)   # intitializing flask app
    app.config['SECRET_KEY'] = 'jfkadfjsdof'

    # need to register blueprints from views and auth
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app 