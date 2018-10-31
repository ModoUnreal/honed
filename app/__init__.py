# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import flask_login
from flask_login import LoginManager

from flask_migrate import Migrate

import logging, os


# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'


"""MAKE A create_app FUNCTION HERE PLES"""

def create_app(debug=False):
    """Initialises the application."""
    # Define the WSGI app object
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Import a module / component using its blueprint handler variable (auth)
    from app.auth.controllers import auth as auth_module
    
    # Register blueprint(s)
    app.register_blueprint(auth_module, url_prefix='/auth')

    return app

# Create the application
app = create_app()

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.auth import controllers, models
