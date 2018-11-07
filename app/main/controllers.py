# Import Flask dependencies
from flask import Blueprint, request, render_template, \
        flash, g, session, redirect, url_for

# Import the database object from the main app module
from app import db

# Import module forms
from app.auth.forms import LoginForm, RegistrationForm

# Define the blueprint; 'main', set its url prefix: app.url/main
main = Blueprint('main', __name__, url_prefix='/main')


@main.route('/index')
def index():
    """View function for the index page, so the main site."""
    return render_template('index.html', title="Honed - The News Website Curated By You.")
