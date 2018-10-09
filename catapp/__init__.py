from flask import Flask
from flask_bootstrap import Bootstrap

from . import catapp
from .catapp import frontend

#   $ flask --app=catapp dev

# We are using the "Application Factory"-pattern here, which is described
# in detail inside the Flask docs:
# http://flask.pocoo.org/docs/patterns/appfactories/

app = Flask(__name__)
Bootstrap(app)

# Our application uses blueprints as well; these go well with the
# application factory. We already imported the blueprint, now we just need
# to register it:
app.register_blueprint(frontend)
# Because we're security-conscious developers, we also hard-code disabling
# the CDN support (this might become a default in later versions):
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['DEBUG'] = True
