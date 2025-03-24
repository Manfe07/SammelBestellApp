import json
import os
import pprint


from app.module_meals.models import db, Restaurant, Mealgroup, Meal

def loadRestaurants():

    basedir = os.path.abspath(os.path.dirname(__file__))
    filePath = os.path.join(basedir,'restaurants.json')  

    with open(filePath) as json_data:
        d = json.loads(json_data.read())
        json_data.close()

        db.session.query(Meal).delete()
        db.session.query(Mealgroup).delete()
        db.session.query(Restaurant).delete()
        db.session.commit()

        rId = 0
        mgId = 0
        mId = 0

        for restaurant in d:

            rId += 1
            newRestaurant = Restaurant(
                id = rId,
                name = restaurant.get('name', 'Unbekannt'),
                description = restaurant.get('description', None),
                phone = restaurant.get('phone', None),
                website = restaurant.get('website', None),
            )
            db.session.add(newRestaurant)

            for mealgroup in restaurant['mealgroups']:
                mgId += 1
                newMealgroup = Mealgroup(
                    id = mgId,
                    number = mealgroup.get('number', 'Unbekannt'),
                    name = mealgroup.get('name', 'Unbekannt'),
                    description = mealgroup.get('description', None),
                    restaurant_id = rId
                )
                db.session.add(newMealgroup)

                for meal in mealgroup['meals']:
                    mId += 1
                    newMeal = Meal(
                        id = mId,
                        number = meal.get('number', '000'),
                        name = meal.get('name', 'Unbekannt'),
                        description = meal.get('description', None),
                        mealgroup_id = mgId,
                        price_1 = meal.get('price_1', 0.0),
                        price_2 = meal.get('price_2', None),
                        price_3 = meal.get('price_3', None),
                    )
                    db.session.add(newMeal)


        db.session.commit()
        