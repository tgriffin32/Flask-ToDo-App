from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path 

# creates database object 
db = SQLAlchemy()
DB_NAME = "database.db "

def create_app():
    app = Flask(__name__)   # intitializing flask app
    app.config['SECRET_KEY'] = 'jfkadfjsdof'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # means our db is store at this location
    db.init_app(app)

    # need to register blueprints from views and auth
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note   

    create_database(app)

    return app 

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')