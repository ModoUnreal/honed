# Import Flask dependencies
from flask import Blueprint, request, render_template, \
        flash, g, session, redirect, url_for

# Import flask_login for the login/logout functions
from flask_login import logout_user, current_user, login_user, login_required

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.auth.forms import LoginForm, RegistrationForm

# Import module models (i.e. User)
from app.auth.models import User

# Define the blueprint; 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """This route is used to login. Uses the login form provided.
       If the @login_required decorator is used on a view function
       then the user will be redirected to this function."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        session['user_id'] = user.id

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Login to Honed', form=form)

@auth.route('/logout')
def logout():
    """View function to log out the user."""
    logout_user()
    return redirect(url_for('index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """View function to register a new user, using the register form."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user) # I have a feeling this might break something, if something breaks then check this line.
        session['user_id'] = user.id
        return redirect(url_for('index'))
    return render_template('auth/register.html', title='Register', form=form)
