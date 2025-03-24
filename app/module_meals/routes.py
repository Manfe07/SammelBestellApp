from flask import render_template

from app.module_meals import bp
from app.module_meals.models import Restaurant, Mealgroup, Meal

from app.extensions import db

@bp.route('/')
def index():
    restaurants = db.session.query(Restaurant)
    return render_template('meals/index.html', restaurants=restaurants)