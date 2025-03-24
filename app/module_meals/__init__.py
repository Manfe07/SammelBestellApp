from flask import Blueprint

bp = Blueprint('meals', __name__, template_folder='templates')

from . import routes, models, tools