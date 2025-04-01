from app.extensions  import db

from app.module_meals.models import Meal
from sqlalchemy import func

class Order(db.Model):
    __tablename__ = 'Order'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer = db.Column(db.String(128), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('Meal.id'), nullable=False)
    size = db.Column(db.String(32), nullable=False)
    notes = db.Column(db.String(128), nullable=True)
    price = db.Column(db.Float, nullable=False)
    payed = db.Column(db.Boolean, nullable=False, default=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    #meal = db.Relationship("Meal", back_populates="orders")
    

#    restaurant = db.Relationship("Restaurant", back_populates="mealgroups")
