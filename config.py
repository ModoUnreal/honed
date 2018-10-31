# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database we are working with
# SQLite will be used
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection against Cross-site Request Forgery (CSRF)
CSRF_ENABLED = True


# NOTE: This is not actually the secret key, don't try.
CSRF_SESSION_KEY = "secret"

# Again not the secret key.
SECRET_KEY = "secret"
