from flask import Blueprint

bp = Blueprint('users', __name__, template_folder='templates')

from . import routes, models, tools

tools.init()