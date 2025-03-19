from flask import Flask, render_template

from app.config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        # Initialize Flask extensions here
        db.init_app(app)
        # Register blueprints here
        import app.module_main as main
        app.register_blueprint(main.bp)
        import app.module_users as users
        app.register_blueprint(users.bp, url_prefix="/users")

        db.create_all()

    @app.route('/test')
    def test():
        return render_template('test.html')


    return app