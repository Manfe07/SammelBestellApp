from flask import render_template, request, redirect, url_for

from app.module_orders import bp
from app.module_orders.models import Order
from app.module_meals.models import Meal

from app.extensions import db

@bp.route('/')
def editOrder():
    meal_id = request.args.get('meal_id')
    meal = db.session.scalar(db.select(Meal).filter_by(id = meal_id))
    if meal:
        return render_template('orders/editOrder.html', meal=meal)
    else:
        return redirect(url_for('meals.index'))