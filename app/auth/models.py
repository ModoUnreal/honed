# Import the database objects (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Define a User model
class User(Base):
    """Represents a user on the website.
       Properties:
       -----------
       id : A unique integer used to identify users.
       username : The unique username a user can have that is seen by others.
       email : The email that will be registered to this account, used to contact.
       password-hash : An encrypted string that will be used to access a user's account.
       """

    __tablename__ = 'auth_user'

    # User Name
    name = db.Column(db.String(128), nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False,
                                          unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Authorisation Data: role & status
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

"""
Note to self:
    I'm assuming what happened was that the variables (say name) have their type first defined (so name is a db.Column instance) and then in __init__ their
    actual value is defined.
    __repr__ is just a magic method that returns a string that contains a printable representation of an object.
"""
