from app.extensions  import db


class Restaurant(db.Model):
    __tablename__ = 'Restaurant'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False) # Changed to db.String to match VARCHAR
    phone = db.Column(db.String(32), nullable=True)
    website = db.Column(db.String(64), nullable=True)

    mealgroups = db.Relationship("Mealgroup", back_populates="restaurant", order_by='Mealgroup.number.asc()')


class Mealgroup(db.Model):
    __tablename__ = 'Mealgroup'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(16), nullable=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id'), nullable=False)

    restaurant = db.Relationship("Restaurant", back_populates="mealgroups")
    meals = db.Relationship("Meal", back_populates="mealgroup")


class Meal(db.Model):
    __tablename__ = 'Meal'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(16), nullable=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=True)
    mealgroup_id = db.Column(db.Integer, db.ForeignKey('Mealgroup.id'), nullable=False)
    price_1 = db.Column(db.Float, nullable=True)
    price_2 = db.Column(db.Float, nullable=True)
    price_3 = db.Column(db.Float, nullable=True)

    mealgroup = db.Relationship("Mealgroup", back_populates="meals")





