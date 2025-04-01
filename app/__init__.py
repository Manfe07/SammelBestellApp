from flask import Flask, render_template
from flask_migrate import Migrate
import os

from app.config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        # Initialize Flask extensions here

        db.init_app(app)
        
        basedir = os.path.abspath(os.path.dirname(__file__))
        MIGRATION_DIR = os.path.join(basedir, 'data', 'migrations')  
        
        migrate = Migrate(app, db, directory=MIGRATION_DIR)
        
        # Register blueprints here
        import app.module_main as main
        app.register_blueprint(main.bp)
        import app.module_users as users
        app.register_blueprint(users.bp, url_prefix="/users")
        import app.module_meals as meals
        app.register_blueprint(meals.bp, url_prefix="/meals")
        import app.module_orders as orders
        app.register_blueprint(orders.bp, url_prefix="/orders")

        db.create_all()
        meals.tools.loadRestaurants()

    @app.route('/test')
    def test():
        return render_template('test.html')


    return app