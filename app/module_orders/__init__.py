from flask import Blueprint

bp = Blueprint('orders', __name__, template_folder='templates')

from . import routes, models