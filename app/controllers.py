# Import Flask dependencies
from flask import Blueprint, request, render_template, \
        flash, g, session, redirect, url_for

# Import flask_login for the login/logout functions
from flask_login import logout_user, current_user, login_user, login_required

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db, app


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    """View function for the index page, so the main site."""
    return render_template('index.html', title="Honed - The News Website Curated By You.")
